from . import db

class AdminAction(db.Model):
    __tablename__ = "ADMIN_ACTION"
    action_id = db.Column(db.Integer, primary_key=True)
    action_taken = db.Column(db.String(100))
    action_date = db.Column(db.Date)
    admin_id = db.Column(db.Integer, db.ForeignKey("USER.user_id"))
    claim_id = db.Column(db.Integer, db.ForeignKey("CLAIM.claim_id"))