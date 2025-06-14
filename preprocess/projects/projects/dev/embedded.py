projects = [
    {
        "title" : "FTC 2024-2025 Season Robot Controller (Renewal)",
        "date" : "2025.6 - 진행 중",
        "summary" : "2024-2025 First Tech Challenge의 오프시즌 대회 Asia-Pacific Open Championship (APOC) 출전 로봇 구동 프로그램",
        "description" : """
            현재 대회를 준비중이며, 개발중에 있습니다. <br>
            <small>이 프로그램은 FTC 2024-2025 Into The Deep 시즌을 위한 코드입니다.</small>
        """,
        "tag" : ["JAVA", "Android", "First Tech Challenge", "Into The Deep", "Robotics"],
        "github" : "",
        "icon" : "../res/projects/FTC.png"
    },
    {
        "title" : "FTC 2024-2025 Season Robot Controller",
        "date" : "2025.1",
        "summary" : "2024-2025 First Tech Challenge의 국내 대회 Korea Robot Championship 출전 로봇 구동 프로그램",
        "description" : """
            객체 지향 프로그래밍을 중심으로 하여 계층적인 구조를 설계하였습니다. 
            로봇을 제어하는 OpMode는 Part에 명령을 전달하고, Part는 동작 명령을 수행합니다.
            Part는 하드웨어를 직접 제어하며, 복잡한 움직임을 통합하여 OpMode에 간단한 명령어 형태로 제공합니다.
            그 외에 비동기적인 기능을 수행하기 위하여 커스텀 Scheduler를 제작하였으며, 
            SmartServo 클래스와 같이 FTC SDK에서 제공하는 하드웨어에 고급 기능을 추가하고 싶은 경우, 
            이를 객체화하여 코드가 중복되지 않도록 하고, 가독성과 효율성을 높였습니다.<br>
            기술적인 부분에서는 PID 제어기를 활용한 정밀한 모터 컨트롤이 가능하도록 하였으며,
            Odometry를 활용한 Localization으로 로봇의 위치를 정밀하게 측정하고, 효과적인 자율주행 시스템을 구축하였습니다.
            또한, OpenCV를 통한 이미지 처리로 오브젝트를 인식하고, 이에 따라 정밀하게 로봇을 컨트롤 할 수 있는 객체 인식 시스템을 제작하였습니다.<br>
            <small>이 프로그램은 FTC 2024-2025 Into The Deep 시즌을 위한 코드입니다.</small>
        """,
        "tag" : ["JAVA", "Android", "First Tech Challenge", "Into The Deep", "Robotics"],
        "github" : "https://github.com/TALOS-25309/FTC2024-2025_RobotSourceCode",
        "icon" : "../res/projects/FTC.png"
    },
    {
        "title" : "FTC 2023-2024 Season Robot Controller (Renewal)",
        "date" : "2024.3 - 2024.4",
        "summary" : "2023-2024 First Tech Challenge의 국제 대회 World Championship 출전 로봇 구동 프로그램",
        "description" : """
            클래스 구조는 FTC 2023-2024 PowerPlay 시즌 코드와 유사합니다.
            단, 로봇 구조가 세계 대회를 준비하며 바뀜에 따라, 이에 맞추어 일부 Part 및 OpMode가 수정되었으며,
            Odometry를 사용할 수 있게 되면서, 바퀴 모터 엔코더 대신에 Odometry 센서에 기반한 정확한 Localization으로
            효과적인 자율주행 시스템을 구축하였습니다. 
            로봇에 설치된 3개의 Odometry 센서 측정값과 로봇 중심으로부터 떨어진 거리를 통합하여
            행렬 연산을 통해 로봇의 정확한 위치와 방향을 구할 수 있는 알고리즘을 고안하였습니다.
            또한, Odometry 센서를 통해 얻어진 위치 방향 피드백을 바탕으로 
            P 제어기를 활용해 로봇이 목표 위치로 정확히 주행하도록 자율 주행 시스템을 보완했습니다.<br>
            <small>이 프로그램은 FTC 2023-2024 CENTERSTAGE 시즌을 위한 코드입니다.</small>
        """,
        "tag" : ["JAVA", "Android", "First Tech Challenge", "CENTERSTAGE", "Robotics"],
        "github" : "https://github.com/TALOS-25309/FTC2023-2024_RobotSourceCode_Renewal",
        "icon" : "../res/projects/FTC.png"
    },
    {
        "title" : "FTC 2023-2024 Season Robot Controller",
        "date" : "2024.1",
        "summary" : "2023-2024 First Tech Challenge의 국내 대회 Korea Robot Championship 출전 로봇 구동 프로그램",
        "description" : """
            클래스 구조는 FTC 2023-2024 PowerPlay 시즌 코드와 유사합니다.
            OpMode는 Part를 제어하고, Part는 Hardware를 제어하며, Hardware는 FTC SDK의 하드웨어들의 고급 기능을 제공합니다.
            각 단계로 올라갈수록 더 통합적인 기능을 수행하며, 단계가 내려갈수록 더 세밀한 조정이 가능합니다.<br>
            이 시즌에서는 IMU를 활용한 로봇의 정밀한 각도 측정을 위해 노력하였습니다.
            이를 통해 얻은 로봇의 각도와 바퀴 모터 엔코더를 기반으로 측정한 위치 정보를 통합하여,
            P 제어기를 통해 정밀한 자율 주행 시스템을 구축하였고, 이는 실제 경기에서 매우 큰 효과를 발휘하였습니다.
            또한 P 제어기를 적극 활용해 중력에 반하여 리니어 슬라이더를 고정하고,
            안정적으로 리니어 슬라이드를 조작할 수 있도록 두 모터의 파워를 Synchronize 할 수 있는 시스템을 구축하여,
            로봇이 기물에 매달리는 파킹 미션을 수행해 경기에서 높은 점수를 얻었습니다.<br>
            <small>이 프로그램은 FTC 2023-2024 CENTERSTAGE 시즌을 위한 코드입니다.</small>
        """,
        "tag" : ["JAVA", "Android", "First Tech Challenge", "CENTERSTAGE", "Robotics"],
        "github" : "https://github.com/TALOS-25309/FTC2023-2024_RobotSourceCode",
        "icon" : "../res/projects/FTC.png"
    },
    {
        "title" : "FTC 2022-2023 Season Robot Controller",
        "date" : "2023.1",
        "summary" : "2022-2023 First Tech Challenge의 국내 대회 Korea Robot Championship 출전 로봇 구동 프로그램",
        "description" : """
            객체 지향 프로그래밍을 적극 활용하여 코드의 가독성을 높이고, 효율을 높이기 위해 노력하였습니다.
            다양한 객체에 계층을 부여하고, 각 객체가 상호작용하도록 하여 코드의 복잡성을 낮추었습니다.
            OpMode는 Part를 제어하고, Part는 Hardware를 제어하며, Hardware는 FTC SDK의 하드웨어들의 고급 기능을 제공합니다.
            각 단계로 올라갈수록 더 통합적인 기능을 수행하며, 단계가 내려갈수록 더 세밀한 조정이 가능합니다.<br>
            또한, 다양한 프로세스의 비동기 처리가 가능하도록 명령이 하달되면 초기 설정만 수행하고 명령을 기억해두었다가, 
            Update 함수를 통해 그 기능을 동시다발적으로 수행할 수 있도록 하였습니다.
            각 계층에 해당하는 클래스는 추상클래스로 묶어, 상위 객체에서 이들을 배열에 저장하여 동적으로 객체를 생성하고 제어할 수 있도록 하였습니다.
            <br>
            <small>이 프로그램은 FTC 2022-2023 Power Play 시즌을 위한 코드입니다.</small>
        """,
        "tag" : ["JAVA", "Android", "First Tech Challenge", "Power Play", "Robotics"],
        "github" : "https://github.com/TALOS-25309/FTC2022-2023_RobotSourceCode",
        "icon" : "../res/projects/FTC.png"
    }
]