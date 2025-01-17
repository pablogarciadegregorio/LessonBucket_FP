from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    birth_date = db.Column(db.String(120), unique=False, nullable=True)
    address = db.Column(db.String(200), unique=False, nullable=True)
    Subjects = db.relationship("Subjects", backref="user", lazy=True)
    Students = db.relationship("Students", backref="user", lazy=True)
    Class = db.relationship("Class", backref="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date,
            "address": self.address,
            
        }
    

class Subjects(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    Subject = db.Column(db.String(120), unique=False, nullable=False)
    Students = db.relationship("Students", backref="subjects", lazy=True)
    Class = db.relationship("Class", backref="subjects", lazy=True)


    def serialize(self):
        return {
            "id": self.id,
            "Subject":  self.Subject,
            "students": list(map(lambda x: x.serialize(), self.Students)),
        
        }


class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    subjects_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    phone = db.Column(db.String(50), unique=False, nullable=False)
    goal = db.Column(db.String(200), unique=False, nullable=False)
    # Comments = db.relationship("Comments", backref="students", lazy=True)
    Class = db.relationship("Class", backref="students", lazy=True)


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "goal": self.goal,
            
        }


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    # comments_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    text_content = db.Column(db.String(200), unique=False, nullable=False)
    
        
        
    def serialize(self):
        return {
            "id": self.id,
            "text_content": self.text_content,
            
        }

class Class(db.Model):
    __tablename__ = 'class'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    subjects_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    comments = db.Column(db.String(240), nullable=True)
    date = db.Column(db.String(120), unique=False, nullable=False)
    hour = db.Column(db.Time(), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    paid = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        subject = Subjects.query.filter_by(id=self.subjects_id).first()
        student = Students.query.filter_by(id=self.student_id).first()
        
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subjects": None if subject is None else subject.serialize(),
            "student": None if student is None else student.serialize(),
            "comments": self.comments,
            "date": self.date,
            "hour": self.hour.strftime("%H:%M"),
            "price": self.price, 
            "paid": self.paid,
        }        
 
    
   