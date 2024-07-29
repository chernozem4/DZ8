class Queries:
    CREATE_COMMENT_TABLE = """
    CREATE TABLE IF NOT EXISTS review_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        visit_date INTEGER,
        instagram_username TEXT,
        food_rating TEXT,
        cleanliness_rating TEXT,
        extra_comments TEXT
    )
    """

    CREATE_TABLE_CATEGORIES = '''
        CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        UNIQUE(name))'''

    CREATE_TABLE_DISHES = '''
        CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255),
        price INTEGER,
        photo TEXT,
        category_id INTEGER,
        UNIQUE(title),
        FOREIGN KEY (category_id) REFERENCES categories (id))'''

    INSERT_INTO_CAT = '''
        INSERT OR IGNORE INTO categories (name) VALUES ('Pepperoni'),('99_cheese'),('Boloneze'), ('Mexicano'), ('4_season'),('Cesar'),('Tay_pizza')'''

    INSERT_INTO_DISHES = '''
        INSERT OR IGNORE INTO dishes (title,price,photo,category_id) VALUES ('Peppa',480,'image/peppa.jpg', 1),
        ('Boloneze',550,'image/Болоньезе.jpg',2),
        ('Mexicano',510,'image/mexicano-2.jpg',3),
        ('99 сыров', 1250, 'image/99 cheese.jpg',4),
        ('Цезарь', 600, 'image/Цезарь.jpg',5),
        ('Тайская', 450, 'image/Тайская.jpg', 6),
        ('4 сезона', 500, 'image/4 ыуфыщт.jpeg', 7)
        '''