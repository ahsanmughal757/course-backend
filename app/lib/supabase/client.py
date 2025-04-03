# import os
# from supabase import create_client, Client
# from supabase.client import ClientOptions
# from dotenv import load_dotenv 

# load_dotenv()

# url: str = os.getenv("SUPABASE_URL")
# key: str = os.getenv("SUPABASE_KEY")


# print("supbase key => ", key)
# print("supbase url => ", url)
# supabase: Client = create_client(url, key,
#     options=ClientOptions(
#         postgrest_client_timeout=10,
#         storage_client_timeout=10,
#         schema="public",
#     ))