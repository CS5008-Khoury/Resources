# Configure GIT on the Khoury Servers
This guide assumes you already setup your account with Khoury, and know how to ssh into the Khoury servers.


## Set up your git on the Khoury servers
You're now on the Khoury servers! A completely different machine from your own computer, and they live across the continent. Type
```console
> ls
```
to see what files are here! (There may not be any.)
If you haven't already, make a directory for CS5008 by typing
```console
> mkdir CS5008
```
Move into this directory by typing 
```console
> cd CS5008
```

Now, we need to do a small bit of setup for your `.gitconfig` file on the Khoury servers. Run these two commands with your Github.com user email and user name in place of the username  and useremail. 
```console
> git config --global user.email "useremail"
> git config --global user.name "username"
```

> WARNING: The following procedure is insecure and should only be used on secure servers on student projects.  This procedure is insecure because it stores your git access token in plaintext. 


Now we need to set the config file so that it will (briefly) store your Personal Access Token (PAT), a sort of temporary password, in your config file.

```console
> git config --global credential.helper 'cache --timeout=604800'
```

The timeout is calculated in seconds. 604,800 is the number of seconds in a week, which would mean you would need to get a new PAT or re-enter your existing PAT on the Khoury servers after 1 week had passed. 

## Get a Personal Access Token from Github.com
Now, we're going to need a Personal Access Token to be able to pull your Github repo onto the Khoury servers. We're following the [instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) from Github.com about how to get a PAT.  

### Let's get that PAT: 
1. Go to Github.com, go to your account in the upper right hand corner, and click on Settings. 
2. Click on Developer Settings
3. Select Personal Access Token (PAT)
4. Name this PAT "Khoury servers", set the expiration for this token to be some time that makes sense to you. I recommend 7 days, because then you only need to get a new PAT once a week. 
5. Select "repo" as the scope.  
6. Generate a PAT, and get ready to copy it in to your terminal that's ssh'd into the Khoury servers, so **that you use it as your password**. 
 
IMPORTANT❗:  Your PAT functions as your password - passwords cannot be used on the Github Command Line Interface (CLI), only PATs and other authentication tokens. 
