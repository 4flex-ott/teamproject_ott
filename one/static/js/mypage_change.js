document.addEventListener('DOMContentLoaded', function() {
    console.log("=== [체크 1] JS 파일 로드 성공 ===");

    const saveBtn = document.getElementById('save_btn');
    const pw1 = document.getElementById('pw1') || document.getElementById('new_pw');
    const pw2 = document.getElementById('pw2') || document.getElementById('confirm_pw');
    const pwMsg = document.getElementById('pw_msg');

    console.log("=== [체크 2] 요소 확인 ===");
    console.log("- 저장버튼:", saveBtn);
    console.log("- 비번1:", pw1);
    console.log("- 비번2:", pw2);

    if (!saveBtn || !pw1 || !pw2) {
        console.error("❌ 에러: HTML에 ID(save_btn, pw1, pw2) 중 하나가 없습니다!");
        return;
    }

    const userEmail = saveBtn.dataset.email || "";
    console.log("- 비교용 이메일:", userEmail);

    function validate() {
        const val1 = pw1.value.trim();
        const val2 = pw2.value.trim();

        console.log(`=== [체크 3] 입력 감지: [${val1}] / [${val2}] ===`);

        const isMatch = (val1.length > 0) && (val1 === val2);
        const isNotEmail = (val1 !== userEmail);

        console.log("- 일치여부:", isMatch);
        console.log("- 이메일과 다름:", isNotEmail);

        if (pwMsg) {
            pwMsg.style.display = "block";
            if (val1 === "" || val2 === "") {
                pwMsg.style.display = "none";
            } else if (!isMatch) {
                pwMsg.textContent = "비밀번호가 일치하지 않습니다.";
                pwMsg.style.color = "#ff153c";
            } else if (!isNotEmail) {
                pwMsg.textContent = "이메일과 동일한 비밀번호는 불가합니다.";
                pwMsg.style.color = "#ff153c";
            } else {
                pwMsg.textContent = "사용 가능한 비밀번호입니다.";
                pwMsg.style.color = "#4caf50";
            }
        }

        // 버튼 활성화 실행
        const finalStatus = !(isMatch && isNotEmail);
        saveBtn.disabled = finalStatus;
        console.log("- 버튼 비활성화(disabled) 여부:", finalStatus);
    }

    pw1.addEventListener('input', validate);
    pw2.addEventListener('input', validate);
});