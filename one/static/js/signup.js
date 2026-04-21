document.addEventListener("DOMContentLoaded", function () {

    // ===== 생년월일 =====
    const yearSelect = document.querySelector("[name='birth_year']");
    const monthSelect = document.querySelector("[name='birth_month']");
    const daySelect = document.querySelector("[name='birth_day']");

    if (yearSelect && monthSelect && daySelect) {

        const currentYear = new Date().getFullYear();

        yearSelect.innerHTML = '<option value="">년도</option>';
        monthSelect.innerHTML = '<option value="">월</option>';
        daySelect.innerHTML = '<option value="">일</option>';

        monthSelect.disabled = true;
        daySelect.disabled = true;

        for (let y = currentYear; y >= currentYear - 100; y--) {
            yearSelect.add(new Option(y + "년", y));
        }

        yearSelect.addEventListener("change", function () {
            const year = this.value;

            monthSelect.innerHTML = '<option value="">월</option>';
            daySelect.innerHTML = '<option value="">일</option>';
            daySelect.disabled = true;

            if (!year) {
                monthSelect.disabled = true;
                return;
            }

            monthSelect.disabled = false;

            for (let m = 1; m <= 12; m++) {
                monthSelect.add(new Option(m + "월", m));
            }
        });

        monthSelect.addEventListener("change", function () {
            const year = yearSelect.value;
            const month = this.value;

            daySelect.innerHTML = '<option value="">일</option>';

            if (!month) {
                daySelect.disabled = true;
                return;
            }

            daySelect.disabled = false;

            const lastDay = new Date(year, month, 0).getDate();

            for (let d = 1; d <= lastDay; d++) {
                daySelect.add(new Option(d + "일", d));
            }
        });
    }

    // ===== 성별 버튼 =====
    const buttons = document.querySelectorAll(".gender-btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", function () {
            buttons.forEach(b => b.classList.remove("active"));
            this.classList.add("active");

            const radio = this.closest("label").querySelector("input");
            if (radio) radio.checked = true;
        });
    });

    // ===== 비밀번호 =====
    const password1 = document.getElementById("password1");
    const password2 = document.getElementById("password2");
    const errorEl = document.getElementById("pw-error");
    const matchMsg = document.getElementById("password-match-msg");

    if (password1 && password2) {

        // 🔹 조건 체크
        function checkPasswordStrength() {
            const pw = password1.value;

            const lengthOk = pw.length >= 8;
            const engOk = /[A-Za-z]/.test(pw);
            const numOk = /[0-9]/.test(pw);
            const specialOk = /[!@#$%^&*]/.test(pw);

            if (!pw) {
                errorEl.textContent = "";
                return;
            }

            if (lengthOk && engOk && numOk && specialOk) {
                errorEl.textContent = "사용 가능한 비밀번호입니다.";
                errorEl.style.color = "#00ff9d";
            } else {
                errorEl.textContent = "영문, 숫자, 특수문자를 포함한 8자 이상으로 입력해주세요.";
                errorEl.style.color = "#ff4d4d";
            }
        }

        // 🔹 일치 체크
        function checkPasswordMatch() {
            const pw1 = password1.value;
            const pw2 = password2.value;

            if (!pw2) {
                matchMsg.textContent = "";
                return;
            }

            if (pw1 === pw2) {
                matchMsg.textContent = "비밀번호가 일치합니다.";
                matchMsg.style.color = "#00ff9d";
            } else {
                matchMsg.textContent = "비밀번호가 서로 다릅니다.";
                matchMsg.style.color = "#ff4d4d";
            }
        }

        // 🔹 이벤트 연결
        password1.addEventListener("input", () => {
            checkPasswordStrength();
            checkPasswordMatch();
        });

        password2.addEventListener("input", checkPasswordMatch);
    }

    // ===== 로그인 비밀번호 보기 =====
    const pwInput = document.getElementById("login-password");
    const toggleBtn = document.getElementById("togglePw");

    if (pwInput && toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            pwInput.type = pwInput.type === "password" ? "text" : "password";
        });
    }

});