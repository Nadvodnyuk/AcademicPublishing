from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Authors(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=True)
    short_name = fields.CharField(max_length=50, null=True)
    code = fields.CharField(max_length=20, null=True, unique=True)
    a_status = fields.CharField(max_length=128, null=True)
    a_country = fields.CharField(max_length=128, null=True)
    a_city = fields.CharField(max_length=128, null=True)
    a_index = fields.IntField(null=True)
    a_adress = fields.CharField(max_length=128, null=True)
    a_org = fields.CharField(max_length=128, null=True)
    a_sub_org = fields.CharField(max_length=128, null=True)
    phone = fields.CharField(max_length=128, null=True)
    email = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.full_name}"


class Works(models.Model):
    id = fields.IntField(pk=True)
    field = fields.CharField(max_length=225)
    title = fields.CharField(max_length=225)
    event = fields.CharField(max_length=225)
    status = fields.CharField(max_length=225)
    year = fields.IntField()
    
    org = fields.CharField(max_length=128)
    sub_org = fields.CharField(max_length=128, null=True)
    country = fields.CharField(max_length=128)
    city = fields.CharField(max_length=128)
    index = fields.IntField()

    mentor = fields.CharField(max_length=225, null=True)
    consultant = fields.CharField(max_length=225, null=True)

    abstract = fields.CharField(max_length=500)
    key_words = fields.CharField(max_length=50)

    intro = fields.TextField()
    aim = fields.TextField()
    materials_methods = fields.TextField()
    results = fields.TextField()
    conclusion = fields.TextField()
    literature = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.title}"


class AuthorsWorks(models.Model):
    id = fields.IntField(pk=True)
    author_id = fields.ForeignKeyField(
        "models.Authors", related_name="work")
    work_id = fields.ForeignKeyField(
        "models.Works", related_name="author")

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.work_id_id}, {self.author_id_id} on {self.created_at}"
