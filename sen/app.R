library(shiny)

# Define the questions and answers
questions_short <- c("한글질문-->영어번역",
                     "영어번역-->chatGPT",
                     "chatGPT-->한글번역")

questions <- c("translate it into English: 중학교에서 수학에서 나오는 연립방정식을 설명해줘",
               "Explain the system of linear equations that come from middle school math",
               "한국어로 번역해주세요:Linear equations are equations that represent a straight line on a graph. They are commonly used in Algebra to solve for the unknown variables within a system of equations. The primary use of linear equations in middle school math is to find the value of an unknown variable or find the relationship between two variables when given the values for the other variables in the equation.
               An example of a linear equation system is the set of equations 2x + y = 4 and 3x + y = 6.
               In this set of equations,
               the two equations are connected and both must be solved to find the values of x and y.
               The solution to this system of equations is x = 2 and y = 2.")

answers <- c("Explain the system of linear equations that come from middle school math",
             "Linear equations are equations that represent a straight line on a graph.
             They are commonly used in Algebra to solve for the unknown variables within a system of equations.
             The primary use of linear equations in middle school math is to find the value of an unknown variable or find the relationship
             between two variables when given the values for the other variables in the equation.
             An example of a linear equation system is the set of equations
             2x + y = 4 and 3x + y = 6. In this set of equations,
             the two equations are connected and both must be solved to find the values of x and y.
             The solution to this system of equations is x = 2 and y = 2.",
             "선형 방정식은 그래프상에 직선을 나타내는 방정식입니다.
             이는 보통 대수학에서 시스템 내부의 알 수 없는 변수를 해결하기 위해 자주 사용됩니다.
             중학교 수학에서 선형 방정식의 주요 용도는 알 수 없는 변수의 값을 찾거나,
             방정식 내의 다른 변수의 값이 주어졌을 때 두 변수 간의 관계를 찾는 것입니다.
             선형 방정식 시스템의 예로는 2x+y=4와 3x+y=6이라는 두 방정식이 존재합니다.
             이 방정식은 서로 연결되어 있고, x와 y의 값을 찾기 위해 두 방정식 모두를 풀어야 합니다.
             이 시스템의 답은 x=2, y=2라는 것입니다.")

# Define the user interface
ui <- fluidPage(
  titlePanel("중2 수학: 연립방정식 개념"),

  sidebarLayout(
    sidebarPanel(
      selectInput("question", "수학 조교(chatGPT) 실행단계", choices = questions_short)
    ),
    mainPanel(
      h3("수학조교(chatGPT) 질문:"),
      textOutput("selected_question"),
      h3("수학조교(chatGPT) 답변:"),
      verbatimTextOutput("answer")
    )
  )
)

# Define the server logic
server <- function(input, output) {


  output$selected_question <- renderText({
    question_idx <- match(input$question, questions_short)
    questions[question_idx]
  })

  output$answer <- renderText({
    idx <- match(input$question, questions_short)
    answers[idx]
  })
}

# Run the app
shinyApp(ui, server)
