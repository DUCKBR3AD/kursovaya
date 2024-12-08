from flask import Flask, render_template, request

app = Flask(__name__)

# Разработчик 1: Данные для расчета
def calculate_cost(material, type_of_furniture, size, features):
    material_prices = {
        'wood': 100,
        'metal': 150,
        'plastic': 80
    }
    
    furniture_types = {
        'cabinet': 300,
        'shelf': 150,
        'drawer': 200
    }

    size_factor = 1 + (size / 100)  # Увеличение цены в зависимости от размера
    feature_factor = 1 + (len(features) * 0.05)  # Увеличение за дополнительные особенности
    
    base_price = material_prices.get(material, 0) + furniture_types.get(type_of_furniture, 0)
    total_cost = base_price * size_factor * feature_factor
    
    return round(total_cost, 2)

# Разработчик 2: Интерфейс (HTML, CSS)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        material = request.form.get("material")
        type_of_furniture = request.form.get("type_of_furniture")
        size = int(request.form.get("size"))
        features = request.form.getlist("features")
        
        # Выполняем расчет
        total_cost = calculate_cost(material, type_of_furniture, size, features)
        
        return render_template("index.html", total_cost=total_cost, material=material, 
                               type_of_furniture=type_of_furniture, size=size, features=features)

    return render_template("index.html", total_cost=None)

if __name__ == "__main__":
    app.run(debug=True)
