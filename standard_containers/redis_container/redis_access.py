import redis

# Connect to redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def set_key_value(key, value):
    return redis_client.set(key, value)


def get_value(key):
    return redis_client.get(key)


def main():
    # set key value pairs.
    set_key_value("name", "pain")
    set_key_value("profession", "pain")
    set_key_value("age", 25)

    # get values for keys
    name = get_value("name").decode("utf-8")
    age = int(get_value("age"))
    print("Name:", name)
    print("Age:", age)


if __name__ == "__main__":
    main()
