package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/coreos/pkg/flagutil"
	"github.com/dghubble/go-twitter/twitter"
	"github.com/dghubble/oauth1"
)

func main() {

	var handle string
	fmt.Printf("enter the username :")
	fmt.Scan(&handle)

	flags := flag.NewFlagSet("user-auth", flag.ExitOnError)
	consumerKey := flags.String("consumer-key", "Cgp32nVbffZW7OOxr9iUzRdmM", "Twitter Consumer Key")
	consumerSecret := flags.String("consumer-secret", "BYE3aytFKyqCaWWB9K0JupNgTbKZYnj2nuq9CfMz14Clohw0gS", "Twitter Consumer Secret")
	accessToken := flags.String("access-token", "1139942391807262721-ynGSBRVBuil9elc0zVMdLJwUdQp7K1", "Twitter Access Token")
	accessSecret := flags.String("access-secret", "UtJIx0iET5epfoHeuuVEFnrmhnOhUBDcSYEOcZfJpfDaj", "Twitter Access Secret")
	flags.Parse(os.Args[1:])
	flagutil.SetFlagsFromEnv(flags, "TWITTER")

	if *consumerKey == "" || *consumerSecret == "" || *accessToken == "" || *accessSecret == "" {
		log.Fatal("Consumer key/secret and Access token/secret required")
	}

	config := oauth1.NewConfig(*consumerKey, *consumerSecret)
	token := oauth1.NewToken(*accessToken, *accessSecret)

	httpClient := config.Client(oauth1.NoContext, token)
	client := twitter.NewClient(httpClient)

	userShowParams := &twitter.UserShowParams{ScreenName: handle}
	user, _, _ := client.Users.Show(userShowParams)
	fmt.Printf("USERS SHOW:\n%+v\n", user)
}
