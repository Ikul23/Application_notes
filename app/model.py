class Note:
    def __init__(self, note_id, title, body, created_date, modified_date):
        self.id = note_id
        self.title = title
        self.body = body
        self.created_date = created_date
        self.modified_date = modified_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_date": self.created_date,
            "modified_date": self.modified_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["body"],
            data["created_date"],
            data["modified_date"]
        )

    def to_list(self):
        return [self.id, self.title, self.body, self.created_date, self.modified_date]
