<h1 align="center">🔐 Password Generator</h1>

<p align="center">
  A simple yet powerful Python application that generates secure, memorable passwords using three memorable words.  
  It allows you to create, view, update, and delete passwords for your apps or websites — all stored locally in a JSON file.  
  <br><br>
  <b>Generate up to 432 unique passwords from just 3 words!</b>
</p>

---

<h2>📜 Features</h2>

<ul>
  <li>Generate strong passwords using 3 memorable words.</li>
  <li>Store credentials (app name, username/email, notes) in a local JSON file.</li>
  <li>View all stored passwords in a clean, readable format.</li>
  <li>Update or delete passwords easily.</li>
  <li>Change your memorable words anytime to generate new combinations.</li>
  <li>Fully offline – no data ever leaves your device.</li>
</ul>

---

<h2>📁 Folder Structure</h2>

<pre>
Password-Generator/
│
├── password_generator.py          # Main application script
├── passwords.json                 # Auto-created data file for storing credentials
├── README.md                      # Documentation
├── LICENSE                        # MIT License
└── assets/
    └── preview.png                # (Optional) Screenshot or demo image
</pre>

---

<h2>⚙️ Installation & Setup</h2>

<ol>
  <li>Ensure you have <b>Python 3.x</b> installed on your system.</li>
  <li>Download or clone this repository:
    <pre><code>git clone https://github.com/your-username/Password-Generator.git</code></pre>
  </li>
  <li>Navigate into the project folder:
    <pre><code>cd Password-Generator</code></pre>
  </li>
  <li>Run the script:
    <pre><code>python password_generator.py</code></pre>
  </li>
  <li>Follow the on-screen instructions to set your memorable words and start generating passwords!</li>
</ol>

---

<h2>🧠 How It Works</h2>

<ul>
  <li>At first launch, you’ll be prompted to enter <b>3 memorable words</b>.</li>
  <li>These words are used in different shuffled combinations to create passwords.</li>
  <li>Each password also includes:
    <ul>
      <li>A random number (0–9)</li>
      <li>A special character (!, @, #, $, %, ^, &, *)</li>
      <li>The app or website name you enter</li>
    </ul>
  </li>
  <li>All information (app name, username, notes, password) is securely stored in a local <code>passwords.json</code> file.</li>
</ul>

---

<h2>🧩 Example</h2>

<pre>
App/Website name: Twitter
Username/email: user@example.com
Notes (optional): personal account

Generated password: AppleSkyRiver4@Twitter
</pre>

---

<h2>🛠️ Available Options</h2>

When running the script, you can choose from:

<pre>
1. Generate password
2. View all passwords
3. Change memorable words
4. Update a password
5. Delete a password
6. Exit
</pre>

---

<h2>🔐 Future Improvements</h2>

<ul>
  <li>Add unique ID fields for easier management of password entries.</li>
  <li>Implement encryption for stored passwords.</li>
  <li>Include validation checks for password strength.</li>
  <li>Add a GUI interface for better user experience.</li>
</ul>

---

<h2>📸 Optional Preview</h2>

<p align="center">
  <img src="assets/preview.png" alt="Application Preview" width="600">
</p>

---

<h2>📄 License</h2>

<p>
  This project is licensed under the <b>MIT License</b> — see the <a href="LICENSE">LICENSE</a> file for details.
</p>

<pre>
MIT License

Copyright (c) 2025 Sheikh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

<h2 align="center">💬 Author</h2>

<p align="center">
  Developed by <b>Sheikh</b> — Learning to Code 🧠  
  <br>
  If you found this helpful, please consider ⭐ starring the repository!
</p>
