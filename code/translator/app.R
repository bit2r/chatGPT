library(shiny)
library(httr)
library(jsonlite)

translate_text <- function(text, source_language, target_language) {
  openai_api_key <- Sys.getenv("OPENAI_API_KEY")

  url <- "https://api.openai.com/v1/engines/chat/completions"

  headers <- add_headers(
    "Content-Type" = "application/json",
    "Authorization" = paste("Bearer", openai_api_key)
  )

  prompt <- paste("Translate the following", source_language, "text to", target_language, ":", text)

  body <- list(
    model = "gpt-3.5-turbo",
    messages = list(
      list(role = "system", content = "You are a helpful assistant that translates text."),
      list(role = "user", content = prompt)
    ),
    max_tokens = 150,
    n = 1,
    stop = NULL,
    temperature = 0.5
  )

  response <- POST(url, headers, body = jsonlite::toJSON(body, auto_unbox = TRUE))
  response_parsed <- content(response, "parsed")

  translation <- response_parsed$choices[[1]]$message$content
  return(translation)
}


translate_text("It's good", "English", "Korean")

ui <- fluidPage(
  titlePanel("Multilingual Translation Tool"),

  sidebarLayout(
    sidebarPanel(
      textInput("text", "Text:"),
      textInput("source_language", "Source Language:"),
      textInput("target_language", "Target Language:"),
      actionButton("translate_button", "Translate")
    ),

    mainPanel(
      verbatimTextOutput("result")
    )
  )
)

server <- function(input, output) {
  observeEvent(input$translate_button, {
    translated_text <- translate_text(input$text, input$source_language, input$target_language)
    output$result <- renderText(translated_text)
  })
}

shinyApp(ui = ui, server = server)
