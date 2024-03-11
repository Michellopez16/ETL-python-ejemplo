

from prefect import flow, task,get_run_logger

@task
def print_hello(name):
    print(f"Hello {name}!")

@flow(name="Hello Flow",log_prints=True)
def hello_world(name="world"):
    #logger = get_run_logger()
    #logger.info("Running the flow")
    print("Iniciando el flujo con la palabra clave log_prints=True")
    print_hello(name)
    #logger.info("Ending the flow")
    print("Terminando el flujo")


if __name__ == '__main__':

    hello_world()
    hello_world("Mundo")