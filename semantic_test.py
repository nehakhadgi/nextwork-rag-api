
import requests

def test_kubernetes_query():
    # 1. Send the POST request to your FastAPI server running on localhost
    response = requests.post("http://127.0.0.1:8000/query?q=What is Kubernetes?")
    
    # 2. Check if the server responded with success
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    # 3. Extract the answer text
    answer = response.json()["answer"]

    # 4. Print the exact answer to your terminal so we can see what TinyLlama returned
    print("\n--- DEBUG: TinyLlama responded with: ---")
    print(answer)
    print("---------------------------------------\n")

    # 5. Run the semantic checks
    assert "orchestration" in answer.lower(), "Missing 'orchestration' keyword"
    assert "container" in answer.lower(), "Missing 'container' keyword"

    print("✅ Kubernetes query test passed")

if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed!")