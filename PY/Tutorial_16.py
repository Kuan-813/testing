
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()  

mongo_uri = os.getenv('MONGODB_ATLAS_CLUSTER_URI')

class DatabaseManager:
    def __init__(self, db_name='example_db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.users_collection = self.db.users
        self.posts_collection = self.db.posts
        self.init_database()

    def init_database(self):
        """Initialize database with collections and indexes"""
        # Create unique index on email for users
        self.users_collection.create_index("email", unique=True)
        # Create index on user_id for posts for better query performance
        self.posts_collection.create_index("user_id")
    
    # Create Function - New User
    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            user_doc = {
                "name": name,
                "email": email,
                "age": age,
                "created_at": datetime.now()
            }
            result = self.users_collection.insert_one(user_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    # Create Function - New Post
    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectOd
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = ObjectId(user_id)
            
            post_doc = {
                "user_id": user_object_id,
                "title": title,
                "content": content,
                "created_at": datetime.now()
            }
            result = self.posts_collection.insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None
    
    # Read Funtion - Get All Users
    def get_all_users(self):
        """Get all users"""
        try:
            users = list(self.users_collection.find())
            # Convert ObjectId to string for display
            for user in users:
                user['_id'] = str(user['_id'])
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

    # Read Function - Get User Post 
    def get_user_posts(self, user_id):
        """Get post by user"""
        try:
            # Convert string user_id to ObjectId if it's valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            posts = list(self.posts_collection.find(
                {"user_id": user_object_id}
            ).sort("created_at", -1))

            # Convert ObjectId to string for display
            for post in posts:
                post['_id'] = str(post['_id'])
                post['user_id'] = str(post['user_id'])
            
            return posts
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []
    
    # Update Function - Update User
    def get_user_by_id(self, user_id):
        """Fetch current data for a specific user"""
        try:
            return self.users_collection.find_one({"_id": ObjectId(user_id)})
        except:
            return None
    
    def update_user(self, user_id, update_data):
        """Update user details"""
        try:
            result = self.users_collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error in updating user: {e}")
            return False
    
    # Update Function - Update Post
    def get_post_by_id(self, post_id):
        """Fetch current post by ID"""
        try:
            return self.posts_collection.find_one({"_id": ObjectId(post_id)})
        except:
            return None
    
    def update_post(self, post_id, update_data):
        """Update post details"""
        try:
            result = self.posts_collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error in updating post: {e}")
            return False

    
    # Delete Function - Delete User
    def delete_user(self, user_id):
        """Delete user and their posts"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            # Delete user's posts first
            self.posts_collection.delete_many({"user_id": user_object_id})

            # Delete the user
            result = self.users_collection.delete_one({"_id": user_object_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
    
    # Close DB Function
    def close_connection(self):
        """Close the MongoDB connection"""
        self.client.close()
    
# Run on Terminal Function
def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("          DATABASE MANAGER")
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
    try:
        db = DatabaseManager()
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Failed to connect MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return
    
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
            print("\n--- Create New Post ---")
            user_id = input("Enter user ID: ").strip()
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            post_id = db.create_post(user_id, title, content)
            if post_id:
                print(f"Post created successfully! ID: {post_id}")
            else:
                print("Failed to create post")
        
        elif choice == '3':
            print("\n--- All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID {user['_id']} | Name: {user['name']} | Email: {user['email']} | Age: {user['age']}")
            else:
                print("No users found.")
        
        elif choice == '4':
            print("\n--- View User Post ---")
            user_id = input("Enter user ID: ").strip()
            posts = db.get_user_posts(user_id)
            if posts:
                for post in posts:
                    print(f"\nPost ID: {post['_id']}")
                    print(f"Title: {post['title']}")
                    print(f"Content: {post['content']}")
                    print(f"Created: {post['created_at']}")
                    print("-" * 30)
            else:
                print("No posts found for this user.")
        
        elif choice == '5':
            print("\n --- Update User Details (leave blank to keep current) ---")
            user_id = input("Enter User ID to update: ").strip()
            current = db.get_user_by_id(user_id)
           
            if current:
                try:
                    name = input(f"Enter new name [{current['name']}]: ").strip() or current['name']
                    email = input(f"Enter new email [{current['email']}]: ").strip() or current['email']
                    age_input = input(f"Enter new age [{current['age']}]: ").strip()
                    age = int(age_input) if age_input else current['age']
                    # Pass update dictionary to the manager
                    if db.update_user(user_id, {"name": name, "email": email, "age": age}):
                        print("User updated succcessfully!")
                    else:
                        print("No changes made to user.")
                except ValueError:
                    print("Invalid age, Please enter a number.")
            else:
                print("User not found.")
        
        elif choice == '6':
            print("\n --- Update Post Details (leave blank to keep current) ---")
            post_id = input("Enter Post ID to update: ").strip()
            current = db.get_post_by_id(post_id)

            if current:
                title = input(f"Enter new title [{current['title']}]: ").strip() or current['title']
                content = input(f"Enter new content [{current['content']}]: ").strip() or current['content']
                # Pass update dictionary to the manager
                if db.update_post(post_id, {"title": title, "content": content}):
                    print("Post updated successfully!")
                else:
                    print("No changes made to user.")
            else:
                print("Post not found.")
        
        elif choice == '7':
            print("\n--- Delete User ---")
            user_id = input("Enter user ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ").strip().lower()
            if confirm == 'y':
                if db.delete_user(user_id):
                    print("User deleted successfully!")
                else:
                    print("User not found of deletion failed.")
            else:
                print("Deletion cancelled.")
        
        elif choice == '8':
            print("\nClosing database connection...")
            db.close_connection()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-8.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()