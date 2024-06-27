class Result:
    def __init__(self):
        self.sentiment = None

    def generate_html(self, sentiment):
        self.sentiment = sentiment
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sentiment Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f8f9fa;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }}
                h1 {{
                    text-align: center;
                    color: #343a40;
                }}
                form {{
                    display: flex;
                    flex-direction: column;
                }}
                label {{
                    margin-bottom: 10px;
                    font-weight: bold;
                    color: #495057;
                }}
                textarea {{
                    padding: 10px;
                    font-size: 16px;
                    margin-bottom: 20px;
                    border: 1px solid #ced4da;
                    border-radius: 4px;
                }}
                input[type="submit"] {{
                    padding: 10px 15px;
                    font-size: 16px;
                    color: #ffffff;
                    background-color: #007bff;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                input[type="submit"]:hover {{
                    background-color: #0056b3;
                }}
                .result {{
                    text-align: center;
                    margin-top: 20px;
                    font-size: 18px;
                    color: #28a745;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Sentiment Analysis</h1>
                <form method="POST">
                    <label for="text">Enter text:</label>
                    <textarea id="text" name="text" rows="4" cols="50" placeholder="Type your text here..."></textarea>
                    <input type="submit" value="Analyze Sentiment">
                </form>
                <div class="result">
                    <h2>Sentiment: {self.sentiment if self.sentiment else ''}</h2>
                </div>
            </div>
        </body>
        </html>
        """
