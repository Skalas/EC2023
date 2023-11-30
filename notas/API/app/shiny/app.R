library(shiny)
library(tidyverse)
library(httr)
library(jsonlite)
library(DT)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Test Dashboard for EC2022"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            textInput("name", h3("Nombre"), 
                     value = "Escriba su nombre"),
            textInput("lastname", h3("Apellido"), 
                     value = "Escriba su nombre"),
            numericInput("age", h3("edad"), value=0),
            actionButton("save", "Guardar"),
        ),

        # Show a plot of the generated distribution
        mainPanel(
           dataTableOutput("users"),
           h2("The flights data"),
           dataTableOutput("flights")    
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    observeEvent(input$save,{
        POST('web:8080/users', body=toJSON(data.frame(name=input$name,lastname=input$lastname, age=input$age)))
    }) 

    output$users = renderDataTable({
        print(input$save)
        resp <- GET('web:8080/')
        df <- fromJSON(content(resp, as='text'))
        df
    })

    output$flights = renderDataTable({
        resp <- GET('web:8080/flights')
        df <- fromJSON(content(resp, as='text'))
        df
    })

}

# Run the application 
shinyApp(ui = ui, server = server)
