from threads import Threads
threads = Threads()

username  = "zuck"

user_id = threads.get_user_id(username=username)

user_info = threads.get_user(id=user_id)

user_threads = threads.get_user_threads(id=user_id)

