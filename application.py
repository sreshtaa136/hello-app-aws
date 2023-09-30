from website import create_app

application = create_app()

if __name__ == '__main__':

    # http://helloapp-env.eba-t9qqrmxm.us-east-1.elasticbeanstalk.com/
    # debug makes sure app is run everytime changes are made to code
    application.run(debug=True)
    