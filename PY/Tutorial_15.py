# TITLE: DATABASE (SQLITE)
# Initialize database:
import sqlite3
class DatabaseManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

    # Creating data (INSERT) - New User
    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None

    # Creating data (INSERT) - New Post
    def create_post(self, user_id, title, content):
        """Create a new post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid
        
    # Read data (SELECT) - Get All Users
    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()
    
    # Read data (SELECT) - Get User Post
    def get_user_posts(self, user_id):
        """Get post by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall()
    
    # Update data (UPDATE) - Update User
    def get_one_user(self, user_id):
        """Fetch current data for a specific user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, email, age FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
    
    def update_user(self, user_id, name, email, age):
        """Update user details"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?', (name, email, age, user_id))
            return cursor.rowcount > 0
    
    # Update data (UPDATE) - Update Post
    def get_post_by_id(self, post_id):
        """Fetch current title and content for a specific post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
            return cursor.fetchone() 

    def update_post(self, post_id, title, content):
        """Update post details"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
            return cursor.rowcount > 0
    
    # Delete data (DELETE) - Delete User
    def delete_user(self, user_id):
        """Delete user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0
    
# Run on Terminal Function:
def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("          DATABADE MANAGER")
    print("="*40)
    print("1. Create User")
    print("2. Create Post")
    print("3. View All Users")
    print("4. View User Posts")
    print("5. Update User")
    print("6. Update Post")
    print("7. Delete User")
    print("8. Exit")
    print("-"*40)
    
def main():
    """Main interactive CLI function"""
    db = DatabaseManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            print("\n--- Create New User ---")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created successfully! ID: {user_id}")
                else:
                    print("Failed to create user")
            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n---Create New Post ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"Post created successfully! ID: {post_id}")
                else:
                    print(f"Failed to create post")
            except ValueError:
                print(f"Invalid user ID. Please enter a number.")
        
        elif choice == '3':
            print("\n--- All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]}")
            else:
                print("No users found.")
        
        elif choice == '4':
            print("\n--- View User Posts ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nPost ID: {post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"Created: {post[3]}")
                        print("-" * 30)
                else:
                    print("No post found for this user")
            except ValueError:
                print("Invalid user ID. Please enter a number")
        
        elif choice == '5':
            print("\n--- Update User Details (Leave blank to keep current) ---")
            try:
                user_id = int(input("Enter user ID to update: ").strip())
                current = db.get_one_user(user_id)
                if current:
                    # current[0]=name | current[1]=email | current[2]=age
                    # Use 'or' to fallback to existing value if input is empty
                    name = input(f"Enter new name [{current[0]}]: ").strip() or current[0]
                    email = input(f"Enter new email [{current[1]}]: ").strip() or current[1]
                    age_input = input(f"Enter new age [{current[2]}]").strip()
                    age = int(age_input) if age_input else current[2]
                    if db.update_user(user_id, name, email, age):
                        print("Successfully updated user details!")
                else:
                    print("User ID not found")
            except ValueError:
                print("Invalid user ID. Please enter a number.")
        
        elif choice == '6':
            print("\n--- Update User Post (Leave blank to keep current) ---")
            try:
                post_id = int(input("Enter user ID to update: ").strip())
                current = db.get_post_by_id(post_id)
                if current:
                    # current[0]=title | current[1]=content 
                    title = input(f"Enter new title [{current[0]}]: ").strip() or current[0]
                    content = input(f"Enter new content [{current[1]}]: ").strip() or current[1]
                    if db.update_post(post_id, title, content):
                        print("Successfully updated user post!")
                    else:
                        print("Post ID not found")
            except ValueError:
                print("Invalid post ID format")

        elif choice == '7':
            print("\n---Delete User ---")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    if db.delete_user(user_id):
                        print("User deleted successfully!")
                    else:
                        print("User not found or deletion failed.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid user ID. Please enter a number.")
        
        elif choice == '8':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")
        
        input("\nPress Enter to continue...")

# Entry point
if __name__ == "__main__":
    main()