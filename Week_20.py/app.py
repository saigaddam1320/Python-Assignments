import os
from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# --- Config ---
# Use env var if provided, else default to local SQLite file
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///products.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- Model ---
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, index=True)
    price = db.Column(db.Float, nullable=False, index=True)
    in_stock = db.Column(db.Boolean, default=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "in_stock": self.in_stock,
            "created_at": self.created_at.isoformat() + "Z",
        }

# Create tables on startup (safe for SQLite dev usage)
with app.app_context():
    db.create_all()

# --- Helpers for common queries ---
def apply_filters(query):
    q = request.args.get("q")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    in_stock = request.args.get("in_stock")

    if q:
        # case-insensitive contains
        query = query.filter(Product.name.ilike(f"%{q}%"))
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if in_stock is not None:
        # accepts "true"/"false" (any case)
        val = in_stock.lower() in ("true", "1", "yes", "y")
        query = query.filter(Product.in_stock == val)
    return query

def apply_sort(query):
    sort = request.args.get("sort", "-created_at")
    mapping = {
        "name": Product.name.asc(),
        "-name": Product.name.desc(),
        "price": Product.price.asc(),
        "-price": Product.price.desc(),
        "created_at": Product.created_at.asc(),
        "-created_at": Product.created_at.desc(),
    }
    return query.order_by(mapping.get(sort, Product.created_at.desc()))

# --- Routes ---

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/products")
def create_product():
    data = request.get_json(force=True, silent=True) or {}
    name = data.get("name")
    price = data.get("price")
    in_stock = data.get("in_stock", True)

    if not name or price is None:
        return jsonify({"error": "name and price are required"}), 400

    try:
        price = float(price)
    except ValueError:
        return jsonify({"error": "price must be a number"}), 400

    p = Product(name=name, price=price, in_stock=bool(in_stock))
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict()), 201

@app.get("/products")
def list_products():
    limit = request.args.get("limit", default=50, type=int)
    query = Product.query
    query = apply_filters(query)
    query = apply_sort(query)
    items = query.limit(min(limit, 200)).all()
    return jsonify([i.to_dict() for i in items])

@app.get("/products/<int:pid>")
def get_product(pid):
    p = Product.query.get_or_404(pid)
    return jsonify(p.to_dict())

@app.put("/products/<int:pid>")
def update_product(pid):
    p = Product.query.get_or_404(pid)
    data = request.get_json(force=True, silent=True) or {}
    if "name" in data and data["name"]:
        p.name = data["name"]
    if "price" in data:
        try:
            p.price = float(data["price"])
        except (TypeError, ValueError):
            return jsonify({"error": "price must be a number"}), 400
    if "in_stock" in data:
        p.in_stock = bool(data["in_stock"])
    db.session.commit()
    return jsonify(p.to_dict())

@app.delete("/products/<int:pid>")
def delete_product(pid):
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"deleted": pid})

# --- Custom aggregate examples ---
@app.get("/products/stats/price")
def price_stats():
    from sqlalchemy import func
    q = apply_filters(Product.query)
    row = q.with_entities(
        func.count(Product.id),
        func.min(Product.price),
        func.avg(Product.price),
        func.max(Product.price),
    ).first()
    count, min_price, avg_price, max_price = row
    return jsonify({
        "count": count or 0,
        "min_price": float(min_price) if min_price is not None else None,
        "avg_price": float(avg_price) if avg_price is not None else None,
        "max_price": float(max_price) if max_price is not None else None,
    })

if __name__ == "__main__":
    app.run(debug=True)
