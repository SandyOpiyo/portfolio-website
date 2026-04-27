<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sandy Opiyo | AI Portfolio</title>

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
        background: #0f172a;
        color: #e2e8f0;
    }

    .container {
        max-width: 1100px;
        margin: auto;
        padding: 20px;
    }

    header {
        text-align: center;
        margin-bottom: 40px;
    }

    header h1 {
        font-size: 2.5rem;
        color: #38bdf8;
    }

    header p {
        color: #94a3b8;
        margin-top: 10px;
    }

    .btn {
        display: inline-block;
        margin-top: 15px;
        padding: 10px 20px;
        background: #38bdf8;
        color: #0f172a;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        transition: 0.3s;
    }

    .btn:hover {
        background: #0ea5e9;
    }

    h2 {
        margin-bottom: 15px;
        color: #38bdf8;
    }

    /* PROJECT GRID */
    .projects {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        margin-bottom: 40px;
    }

    /* CARD */
    .card {
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 10px 20px rgba(0,0,0,0.4);
    }

    .card h3 {
        margin-bottom: 10px;
        color: #f1f5f9;
    }

    .card p {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .card a {
        color: #38bdf8;
        text-decoration: none;
        font-weight: bold;
    }

    .card a:hover {
        text-decoration: underline;
    }

    /* SKILLS */
    .skills {
        margin-bottom: 40px;
    }

    .skills span {
        display: inline-block;
        background: #1e293b;
        padding: 8px 15px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }

    /* CONTACT */
    .contact {
        text-align: center;
        margin-top: 30px;
    }

    footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #64748b;
    }
</style>
</head>

<body>

<div class="container">

<header>
    <h1>Sandy Opiyo</h1>
    <p>Junior AI Specialist | Data Analyst | Python Enthusiast</p>
    <a href="#" class="btn">Download CV</a>
</header>

<section>
    <h2>🚀 Projects</h2>

    <div class="projects">

        <div class="card">
            <h3>Customer Purchase Prediction</h3>
            <p>Machine learning model predicting customer buying behavior using logistic regression.</p>
            <a href="https://github.com/Sandy Opiyo/customer-purchase-prediction">View Project →</a>
        </div>

        <div class="card">
            <h3>Sales Data Analysis</h3>
            <p>Analyzed sales trends and identified top-performing products using Python.</p>
            <a href="https://github.com/SandyOpiyo/sales-data-analysis">View Project →</a>
        </div>

        <div class="card">
            <h3>AI Chatbot</h3>
            <p>Simple rule-based chatbot simulating human interaction using Python.</p>
            <a href="https://github.com/Sandy Opiyo/ai-chatbot">View Project →</a>
        </div>

    </div>
</section>

<section class="skills">
    <h2>⚙️ Skills</h2>
    <span>Python</span>
    <span>Machine Learning</span>
    <span>Data Analysis</span>
    <span>SQL</span>
    <span>Pandas</span>
    <span>Scikit-learn</span>
</section>

<section class="contact">
    <h2>📞 +254 705402825</h2>
    <p>Email: opiyosandy@gmail.com</p>
</section>

<footer>
    <p>© 2026 Sandy Opiyo | AI Portfolio</p>
</footer>

</div>
<script>
// Typing effect
const text = "Junior AI Specialist | Data Analyst | Python Enthusiast";
let i = 0;

function typeEffect() {
    if (i < text.length) {
        document.getElementById("typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeEffect, 50);
    }
}
typeEffect();

// Scroll animation
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
});

document.querySelectorAll('.hidden').forEach(el => observer.observe(el));
</script>

</body>
</html>

        
