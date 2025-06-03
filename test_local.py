from main import predict
import time

# Local test without Cerebrium
with open("assets/test_fashion.jpg", "rb") as f:
    start = time.time()
    results = predict(f.read())
    latency = (time.time() - start) * 1000

print(f"Local prediction ({(latency):.1f}ms):")
for res in results:
    print(f"- {res['label']}: {res['score']:.2%}")
