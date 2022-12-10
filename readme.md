# Not ready for use

### Keep in mind
This project is a work in progress and is in initial concept stage.

This project needs to be split into two different applications in the future
- Theme - uswds_theme: This will be a quickstart theme that get your project up and going for custom front end development.
- USWDS_CORE - uswds: This will house majority the custom plugins that are designed to work together out the box.

## Useful documentation
- https://docs.django-cms.org/
- https://docs.lando.dev/
- https://docs.djangoproject.com/en/4.1/
- https://designsystem.digital.gov/

### Local Development
To get the local development started we have included a Lando configuration.
More about Lando https://docs.lando.dev/

#### Todo: Create a docker-compose for local development.

### Getting started with Lando
```
cd into/your/project/root/path
# Running this command the first time will create the images you need.
# This command might take some time to finish the first time.
lando start

# After it has successfully shown you the start up URLs
lando manage migrate
lando manage createsuperuser
lando restart
```

Should now navigate to http://uswds-djangocms.lndo.site/admin to login with the user you created.


