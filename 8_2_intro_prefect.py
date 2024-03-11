from prefect import flow, task

@task
def print_hello(name):
    print(f"Hello {name}!")

@flow(name="Hello Flow")
def hello_world(name="world"):
    print_hello(name)


if __name__ == '__main__':
    hello_world()
    hello_world("Mundo")
    


