from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = '''
<!doctype html>
<html>
<head>
    <title>Temperature Converter</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .box { border: 1px solid #ccc; padding: 20px; max-width: 400px; border-radius: 5px; }
        input, button { margin-top: 10px; padding: 8px; width: 100%; box-sizing: border-box; }
        .result { margin-top: 15px; font-weight: bold; color: green; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Temperature Converter</h1>
        
        <h3>Celsius to Fahrenheit</h3>
        <form method="post" action="/c-to-f">
            <input type="number" step="any" name="celsius" placeholder="Enter Celsius" required>
            <button type="submit">Convert to Fahrenheit</button>
        </form>

        {% if result is not none %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.get("/")
def home():
    return render_template_string(PAGE, result=None)

@app.post("/c-to-f")
def c_to_f():
    try:
        celsius = float(request.form.get("celsius", 0))
        fahrenheit = (celsius * 9/5) + 32
        result_text = f"{celsius}°C is equal to {fahrenheit:.2f}°F"
    except ValueError:
        result_text = "Invalid input."
    return render_template_string(PAGE, result=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
