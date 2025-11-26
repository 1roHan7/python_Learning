# Airflow Tutorial

## Airflow Installation and Setup

**STEPS**

- Create a **Virtual Environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

- Run below command to **Install Airflow**

```bash
pip install "apache-airflow[celery]==3.1.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.3/constraints-3.12.txt"
```

```bash
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
```

- **Setup Airflow DB** for storing Airflow Metadata

```bash
airflow db migrate
```

In newer versions of Airflow, the DB already gets created without this command.

- **Create an admin user**

```bash
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```

> **Note:** The `airflow users` command doesn't exist in Airflow 2.8+. This is because Airflow 2.8+ removed the `users` command.
> 
> In newer versions, you need to use the **Airflow Standalone** command or the **Web UI** to create users.
> 
> **Option 1: Use Airflow Standalone (Easiest)**
> 
> ```bash
> airflow standalone
> ```
> 
> This command will:
> - Initialize the database
> - Create a default admin user automatically
> - Start the web server and scheduler together
> 
> The output will show the admin credentials.

- **Start the Airflow web server**

```bash
airflow webserver --port 8080
```

- **In another terminal, start the scheduler**

```bash
airflow scheduler
```

- **Access Airflow UI**

http://localhost:8080

- **Verify everything is working:**

```bash
# Check Airflow version
airflow version

# List all DAGs
airflow dags list
```