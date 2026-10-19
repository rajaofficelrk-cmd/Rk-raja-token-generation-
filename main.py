
import os
import secrets
from datetime import timedelta
from flask import (
    Flask, render_template_string, jsonify,
    redirect, request, session, url_for
)

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "0") == "1",
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30),
    MAX_CONTENT_LENGTH=16 * 1024
)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#080812">
<title>RK RAJA HERE | Token Tool</title>

<style>
:root {
    --bg: #080812;
    --card: rgba(20, 20, 42, .88);
    --cyan: #00eaff;
    --pink: #ff00dd;
    --green: #00ff95;
    --muted: #a9aec5;
}

* { box-sizing: border-box; }

body {
    margin: 0;
    min-height: 100vh;
    padding: 20px;
    color: #fff;
    background:
        radial-gradient(ellipse at 10% 10%, #10275b 0%, transparent 42%),
        radial-gradient(ellipse at 90% 90%, #3b0845 0%, transparent 40%),
        var(--bg);
    font-family: system-ui, Arial, sans-serif;
    overflow-x: hidden;
}

#particles {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
}

.particle {
    position: absolute;
    bottom: -15px;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--cyan);
    opacity: .45;
    animation: rise linear infinite;
}

@keyframes rise {
    from { transform: translateY(0); opacity: 0; }
    15% { opacity: .45; }
    to { transform: translateY(-110vh); opacity: 0; }
}

.container {
    position: relative;
    z-index: 1;
    max-width: 1050px;
    margin: auto;
}

.header {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 34px 14px;
    border: 2px solid var(--cyan);
    border-radius: 24px;
    background:
        radial-gradient(ellipse at 50% 0%, #182c61, transparent 70%),
        linear-gradient(145deg, #080812, #16162c);
    box-shadow: 0 0 22px #00d9ff55;
    animation: borderGlow 5s linear infinite;
}

.header::after {
    content: "";
    position: absolute;
    width: 200%;
    height: 100%;
    top: 0;
    left: -220%;
    pointer-events: none;
    background: linear-gradient(
        100deg, transparent, #ffffff12, transparent
    );
    animation: shine 6s linear infinite;
}

.crown, .logo, .here, .live, .tagline {
    position: relative;
    z-index: 1;
}

.crown {
    font-size: 48px;
    color: #ffe600;
    text-shadow: 0 0 18px #ff9900;
    animation: float 2s ease-in-out infinite;
}

.logo {
    margin: 4px 0;
    font-size: clamp(36px, 9vw, 76px);
    line-height: 1.15;
    font-weight: 1000;
    font-style: italic;
    letter-spacing: 3px;
    background: linear-gradient(
        90deg, #ff1744, #ffe600, #00eaff,
        #a855ff, #ff00dd, #ff1744
    );
    background-size: 300% 100%;
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    filter: drop-shadow(0 0 10px #008cff);
    animation: rainbow 4s linear infinite;
}

.here {
    font-size: clamp(24px, 6vw, 40px);
    font-weight: 900;
    letter-spacing: 9px;
    text-shadow: 0 0 15px var(--cyan);
    animation: pulse 1.8s infinite;
}

.live {
    display: inline-block;
    margin-top: 20px;
    padding: 9px 16px;
    border: 1px solid var(--green);
    border-radius: 30px;
    color: var(--green);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    box-shadow: 0 0 12px #00ff8833;
}

.dot {
    display: inline-block;
    width: 9px;
    height: 9px;
    margin-right: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 12px var(--green);
    animation: blink 1s infinite;
}

.tagline {
    margin-top: 18px;
    color: #d9d9ff;
    font-size: 12px;
    letter-spacing: 3px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
    margin-top: 22px;
}

.card {
    min-width: 0;
    padding: 24px;
    border: 1px solid #ffffff1c;
    border-radius: 20px;
    background: var(--card);
    box-shadow: 0 12px 35px #0005;
    backdrop-filter: blur(12px);
}

.card h2 {
    margin-top: 0;
    font-size: 21px;
}

.card p {
    color: var(--muted);
    line-height: 1.7;
}

.feature {
    display: flex;
    align-items: flex-start;
    gap: 13px;
    margin: 18px 0;
}

.feature-icon {
    display: grid;
    place-items: center;
    flex: 0 0 42px;
    height: 42px;
    border: 1px solid #00eaff55;
    border-radius: 12px;
    background: #00eaff0d;
    font-size: 21px;
}

.feature strong { display: block; }
.feature small { color: var(--muted); line-height: 1.5; }

.info {
    padding: 15px;
    border: 1px solid #00eaff44;
    border-radius: 12px;
    background: #00eaff0b;
    color: #d9faff;
    font-size: 14px;
    line-height: 1.7;
}

.btn {
    display: block;
    width: 100%;
    margin-top: 18px;
    padding: 15px;
    border: 0;
    border-radius: 12px;
    background: linear-gradient(90deg, #0866ff, #00c6ff);
    color: white;
    font-size: 15px;
    font-weight: 800;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    transition: transform .2s, filter .2s;
}

.btn:hover {
    transform: translateY(-2px);
    filter: brightness(1.13);
}

.status {
    min-height: 24px;
    margin-top: 15px;
    color: var(--green);
    font-size: 13px;
    overflow-wrap: anywhere;
}

.status.error { color: #ff647c; }

.badge {
    display: inline-block;
    padding: 5px 10px;
    border: 1px solid #00ff9555;
    border-radius: 20px;
    color: var(--green);
    font-size: 11px;
    font-weight: bold;
}

footer {
    margin: 25px 0 8px;
    color: #9295ad;
    font-size: 12px;
    line-height: 1.8;
    text-align: center;
}

@keyframes rainbow {
    to { background-position: 300% 0; }
}

@keyframes borderGlow {
    0%, 100% {
        border-color: var(--cyan);
        box-shadow: 0 0 20px #00eaff44;
    }
    50% {
        border-color: var(--pink);
        box-shadow: 0 0 24px #ff00dd55;
    }
}

@keyframes float {
    50% { transform: translateY(-6px); }
}

@keyframes pulse {
    50% { opacity: .65; }
}

@keyframes blink {
    50% { opacity: .25; }
}

@keyframes shine {
    0% { left: -220%; }
    35%, 100% { left: 120%; }
}

@media (max-width: 700px) {
    body { padding: 12px; }
    .grid { grid-template-columns: 1fr; }
    .card { padding: 20px; }
    .header { padding: 28px 10px; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>
<div id="particles" aria-hidden="true"></div>

<div class="container">
    <header class="header">
        <div class="crown">♛</div>
        <div class="logo">RK RAJA</div>
        <div class="here">HERE</div>
        <div class="live">
            <span class="dot"></span> LIVE ANIMATION
        </div>
        <div class="tagline">⚡ OFFICIAL • SECURE • SIMPLE ⚡</div>
    </header>

    <div class="grid">
        <section class="card">
            <span class="badge">RK RAJA PROJECT</span>
            <h2>Welcome to the Tool</h2>
            <p>
                A neon-styled demo dashboard built with Flask.
                Use official authorization for any account connection.
            </p>

            <div class="info">
                <strong>🔐 Account Safety</strong><br>
                This demo never asks for your Facebook password or
                OTP. It does not collect login cookies or extract
                account tokens.
            </div>

            <a class="btn" href="{{ facebook_url }}">
                Continue to Official Facebook
            </a>

            <div class="status" id="status" role="status">
                {{ auth_status }}
            </div>
        </section>

        <section class="card">
            <h2>⚡ Features</h2>

            <div class="feature">
                <div class="feature-icon">👑</div>
                <div>
                    <strong>RK RAJA Branding</strong>
                    <small>Animated rainbow title and neon effects.</small>
                </div>
            </div>

            <div class="feature">
                <div class="feature-icon">📱</div>
                <div>
                    <strong>Mobile Friendly</strong>
                    <small>Responsive layout for phone and desktop.</small>
                </div>
            </div>

            <div class="feature">
                <div class="feature-icon">🛡️</div>
                <div>
                    <strong>Privacy First</strong>
                    <small>No password or OTP collection in this demo.</small>
                </div>
            </div>

            <div class="feature">
                <div class="feature-icon">⚙️</div>
                <div>
                    <strong>Flask Backend</strong>
                    <small>Health endpoint and deployment support.</small>
                </div>
            </div>
        </section>
    </div>

    <footer>
        RK RAJA HERE • Built with Flask<br>
        Use only authorized account integrations.
    </footer>
</div>

<script>
(function () {
    const root = document.getElementById("particles");
    for (let i = 0; i < 32; i++) {
        const particle = document.createElement("span");
        particle.className = "particle";
        particle.style.left = (Math.random() * 100) + "%";
        particle.style.animationDuration =
            (8 + Math.random() * 14) + "s";
        particle.style.animationDelay =
            (-Math.random() * 18) + "s";
        particle.style.opacity = (0.15 + Math.random() * 0.4);
        root.appendChild(particle);
    }
})();
</script>
</body>
</html>
"""

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/")
def index():
    # Official OAuth integration is intentionally not configured
    # until a real Meta app and its approved permissions are set up.
    facebook_url = os.environ.get("FACEBOOK_OAUTH_URL", "")
    auth_status = (
        "Official authorization URL configured."
        if facebook_url.startswith("https://")
        else "Demo mode: official Facebook OAuth is not configured."
    )

    if not facebook_url.startswith("https://"):
        facebook_url = "#"

    return render_template_string(
        HTML,
        facebook_url=facebook_url,
        auth_status=auth_status
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(413)
def too_large(error):
    return jsonify({"error": "Request too large"}), 413


@app.errorhandler(500)
def internal_error(error):
    app.logger.error("Internal server error")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
