from backend import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text
        )

    def __repr__(self):
        return '<Task id={id} title={title!r}>'.format(
            id=self.id, title=self.title)

class Feed(db.Model):
    __tablename__ = 'feeds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    url = db.Column(db.Text)
    description = db.Column(db.Text)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            url=self.url,
            description=self.description
        )

    def __repr__(self):
        return '<Feed id={id} name={name!r} url={url!r} description={description!r}>'.format(
            id=self.id, name=self.name, url=self.url, description=self.description)

def init():
    db.create_all()
