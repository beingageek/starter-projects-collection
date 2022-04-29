package main

import (
	"net/http"
  
	"github.com/gin-gonic/gin"
  )

func main() {
	r := gin.Default()
	r.LoadHTMLFiles("pages/index.html")
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title": "Home Page",
		})
	})
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run() // listen and serve on localhost:8080
}