CHANELLOG

Version 0.1., Release Date: 24th August 2018, initial version

Version 0.2. Release Date: 29th August 2018.
CHANGES in version 0.2:
-the entire website now uses djangos authentication system
-additional information for the user is added after the initial registration
KNOWN BUGS:
-If the user has more than one product, the my profile section crashes the website(to be adressed in v 0.2.1)

Version 0.2.1., Release Date: 31st august 2018.
CHANGES in version 0.2.1.:
-You can now see other users profiles just like you can view your own(if you try to acess your own profile that way you will be brought to the My Profile page)
-You can now acess the homepage from anywhere on the website by using the Homepage button in the upper right corner(it has the distinct red color)
-To post products, you now have to fill out the additional user information in the My Profile section
-All forms got the visual overhaul
-Add a product and Login pages now have the same look treatment as the rest of the website
BUGFIXES:
-User is no longer able to login again by typing the url for the login page
-It is no longer possible to have 2 users with same usernames
-It is no longer possible to acess the My Profle page via the url if the user is not logged in
KNOWN BUGS:
2 products are still able to have same names, therefore it crashes the website if the user tries to acess one of those products(to be adressed inthe next update)

MAJOR ANNOUNCEMENT:
-Besides the next smaller update, version 0.2.2., version 0.3 is in development
-There are new features coming to that version, including the user rating system(Its pieces of code can already be seen in version 0.2.1., although they are commented out)
-Excpect more information soon!

Version 0.2.2., finished but unreleased, will be mered into version 0.2.3.

Version 0.2.3., release date: 8th September 2018.

Changes in Version 0.2.3.(Definitive Edition):
-All new and improved, responsive design, designed with the help of bootstrap(NOTE: not the final design)
-Visual changes on all templates, especially the my profile and product detail pages
-The my profile and logout buttons are now under the new dropdown menu when the user click the user icon
-All forms got the slight visual overhaul
-The bootstrap responsive navigation bar
-The About page has been added
-The product can now have up to 5 images, which are all responsive(although there is some work to be done there)
KNOWN BUGS:
-Images are not deleted when the product is deleted(to be fixed in the next update)
NEWS:
Versions from 0.2.4. onwards will focus only on the backend changes, front end will be improved at some point but is currently not the focus

Version 0.2.4., release date: 15th september 2018.

Changes in Version 0.2.4.
-KEY FEATURE: The ability to edit or delete the already posted product(The user can edit anything except the sub category)
-BUGFIXES:
 -Images are now deleted when the product is deleted
 
 
Version 0.3., release date: 22nd september 2018.

Changes in Version 0.3.
-New major release
-You can now rate other users:
-you cannot rate the user twice
-the rating cannot be greater than 5 or lesser than 1
-You cannot rate Yourself
-You cannot rate the user if the user did not post any products
-You can now comment on other users products:
-No more than 1 comment per user
-You cannot comment on your own product

-NOTE: Instead of waiting for new changes on github, you can experience the latest changes by going to:
http://redhat.pythonanywhere.com/items/
On GitHub, the most stable code will be released, the website is used for testing purposes and coding on the go(aka. school when i have free time with the PC haha)
Those changes can be quite buggy though, so be free to report any bugs to me!

-MAJOR ANNOUNCMENT: Next major release, the version 0.4. will take at least a few weeks to make since I am working on other projects that have a deadline and I must finish them, and school is also keeping me away from coding(i hate it for it)
