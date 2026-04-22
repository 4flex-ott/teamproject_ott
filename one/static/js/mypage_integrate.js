document.addEventListener('DOMContentLoaded', function() {
    console.log("계정 통합 JS 로드 완료");

    const form = document.querySelector('.edit-form');
    const pw1 = document.getElementById('pw1');
    const pw2 = document.getElementById('pw2');
    const pwMsg = document.getElementById('pw_msg');
    const saveBtn = document.getElementById('save_btn');
    const userEmail = saveBtn.dataset.email;

    // 성별 버튼 처리
    const genderLabels = document.querySelectorAll('.gender-btn');
    genderLabels.forEach(label => {
        label.addEventListener('click', function() {
            genderLabels.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            validate(); // 성별 선택 시에도 검증 실행
        });
    });

    function validate() {
        const val1 = pw1.value.trim();
        const val2 = pw2.value.trim();

        // 1. 비밀번호 일치 검사
        let isPwMatch = false;
        if (val1.length > 0 && val2.length > 0) {
            if (val1 === val2) {
                pwMsg.style.display = 'none';
                isPwMatch = true;
            } else {
                pwMsg.style.display = 'block';
                pwMsg.textContent = "⚠️ 비밀번호가 일치하지 않습니다.";
                isPwMatch = false;
            }
        } else {
            pwMsg.style.display = 'none';
        }

        // 2. 이메일과 동일한 비밀번호 방지
        if (val1 === userEmail) {
            pwMsg.style.display = 'block';
            pwMsg.textContent = "⚠️ 이메일과 동일한 비밀번호는 사용할 수 없습니다.";
            isPwMatch = false;
        }

        // 3. 모든 필수 필드 입력 여부 확인 (HTML5 checkValidity 사용)
        const isFormValid = form.checkValidity();

        // 최종 조건: 모든 필드 채워짐 + 비밀번호 일치
        saveBtn.disabled = !(isFormValid && isPwMatch);
    }

    // 모든 input 요소에 입력 시 검증 함수 실행
    form.querySelectorAll('input').forEach(input => {
        input.addEventListener('input', validate);
    });

    // 초기 실행
    validate();
});

// 서브밋 시 최종 방어 코드
function validatePassword() {
    const pw1 = document.getElementById('password1').value;
    const pw2 = document.getElementById('pw2').value;
    if (pw1 !== pw2) {
        alert("비밀번호가 일치하지 않습니다.");
        return false;
    }
    return true;
}