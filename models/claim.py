from . import db

class Claim(db.Model):
    __tablename__ = "CLAIM"
    claim_id = db.Column(db.Integer, primary_key=True)
    claim_date = db.Column(db.Date)
    proof_description = db.Column(db.Text)
    claim_status = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("USER.user_id"))
    item_id = db.Column(db.Integer, db.ForeignKey("FOUND_ITEM.item_id"))