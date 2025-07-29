# 6. Movie Recommendation Page 
#  Requirements: 
#  /movies shows recommended movies from Flask list 
#  Loop through movie list and render posters and titles 
#  Use conditional to show “New Release” tag if applicable 
#  Load rating stars using a static/images/star.png 
#  Shared layout and styles via base.html and style.css 

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/movies")
def movies():
    recommended = [
        {"title": "Amaran", "poster": "Amaran.jpg", "new": True},
        {"title": "Gilli", "poster": "gilli.jpg", "new": False},
        {"title": "Theri", "poster": "Theri.jpg", "new": False}
    ]
    return render_template("movies.html", movies=recommended)

if __name__ == "__main__":
    app.run(debug=True)
