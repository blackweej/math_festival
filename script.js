document.addEventListener('DOMContentLoaded', function(){
    const sectionsContainer = document.getElementById('sections');

    
    
    let selectedResults = {
        'gr': 0,
        'hu': 0,
        're': 0,
        'sl': 0
    };
    
     let playerName = ""; // 이름을 저장할 변수
    playerName = prompt("이름을 입력하세요:");
    
   const questions = [
        "포션을 통해서 한 가지 능력을 얻을 수 있다면?",
        "한 가지 물건을 고르기",
        "좋아하는 색",
        "나와 가장 속성이 비슷한 원소",
        "내가 가장 중요하게 생각하는 가치",
        "다른 친구가 나와 가장 친한 친구를 괴롭혀 다치게 했다면",
        "내가 원하는 기숙사 입구의 위치",
        "원하는 사감 선생님의 성격",
        "담임선생님 과목은?",
        "호그와트를 침입해온 적들과 전투가 벌어졌다. 전투에 참여하게 된다면 그 이유는?"
    ];

    const choices = [
        ["모두를 설득할 수 있는 화술", "모든 문제를 풀 수 있는 지능", "다른 사람의 말의 진위 여부를 판단할 수 있는 능력", "어떠한 상황에서도 최고의 결정을 내릴 수 있는 판단력"],
        ["물약", "검", "지팡이", "망토"],
        ["검정색","청동색","은색","금색"],
        ["불","흙","공기","물"],
        ["협동","대담함","창의성","의지력"],
        ["괴롭힌 친구를 욕한다","다친 내 친구를 먼저 보건실에 데려다준다","괴롭힌 친구를 복수해준다","내 친구가 다시는 괴롭힘 받지 않도록 지켜준다"],
        ["지하실","그림 안","벽 안","동상 아래"],
        ["엄격하지만 은근 잘 챙겨주는 선생님","적어도 우리에게는 잘해주는 선생님","착하시고 잘 챙겨주시는 선생님","수업 잘 해주시는 선생님"],
        ["물리","화학","생명과학","지구과학"],
        ["전쟁에서 공을 세우면 나에게 돌아오는 것이 많을 것이기 때문이다","나의 실력을 뽐낼 수 있는 기회라고 생각하기 때문이다","참여하는 것이 옳은 일이라고 생각하기 때문이다","맞서 싸우는 것이 진정한 마법사라고 생각하기 때문이다"]
    ];
    
    const classfic ={
        'gr' : 0,
        'hu' : 1,
        're' : 2,
        'sl' : 3,
    }

    const results = [
        ['sl','re','hu','gr'],
        ['re','gr','hu','sl'],
        ['hu','re','sl','gr'],
        ['gr','hu','re','sl'],
        ['hu','gr','re','sl'],
        ['sl','hu','gr','re'],
        ['hu','gr','sl','re'],
        ['gr','sl','hu','re'],
        ['gr','sl','hu','re'],
        ['sl','re','hu','gr']
    ];

        for (let i = 0; i < questions.length; i++) {
        const section = document.createElement('div');
        section.classList.add('section');

        const question = document.createElement('div');
        question.textContent = questions[i];
        section.appendChild(question);

        const choicesContainer = document.createElement('div');
        choicesContainer.classList.add('choices');
        section.appendChild(choicesContainer);

        const boxes = [];
        for (let j = 0; j < 4; j++) {
            const choiceBox = document.createElement('div');
            choiceBox.classList.add('box');
            choiceBox.textContent = choices[i][j];
            boxes.push(choiceBox);
            choicesContainer.appendChild(choiceBox);

            choiceBox.addEventListener('click', function() {
                // 기존에 선택되었던 선택지의 배경색 초기화
                boxes.forEach(box => box.style.backgroundColor = "white");

                // 선택한 선택지의 배경색 변경
                choiceBox.style.backgroundColor = "#6CDF65";

                const selectedResult = results[i][j];
                selectedResults[selectedResult]++;
            });
        }
        
        sectionsContainer.appendChild(section);
    }

    const endButton = document.createElement('button'); // "end" 버튼 생성
    endButton.textContent = "end";
    endButton.style.marginTop = "10px";
    endButton.style.fontSize = "25px";
    sectionsContainer.appendChild(endButton);
    
        endButton.addEventListener('click', function() {
        console.log(`${playerName} ${selectedResults['gr']} ${selectedResults['hu']} ${selectedResults['re']} ${selectedResults['sl']}`);
        alert("설문조사가 끝났습니다")
    });
});

