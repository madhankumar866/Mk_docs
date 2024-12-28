#
## Combine Multiple Git Commits into One:

- To merge multiple commits into one in Git, you can use an interactive rebase. Here's how you can do it:


1.Open your terminal or command prompt.

2.Navigate to the Git repository where you want to merge the commits.

3.Ensure you have a clean working directory. Commit or stash any changes you have in progress.

4.Run the following command to initiate an interactive rebase:

!!! Command 
        git rebase -i HEAD~n

- Replace n with the number of commits you want to merge. For example, if you want to merge the last 3 commits, you'd use HEAD~ ^^"Replace_With_Any_Number"^^

5.Run the following command to initiate an interactive rebase, starting from the commit just before the one you want to move 

!!! Command
       git rebase -i ^^Last_Commit^^

This opens a text editor with a list of commits starting from ^^Last_Commit^^ and going back in time.

6.In the list of commits, locate the commit you want to move to the last position (let's call it ^^Last_Modified^^). It will look something like this:

!!! Terminal Message
      pick ab12c34 Commit message 1

      pick de56f78 Commit message 2

      pick gh90i12 Commit message 3

7.Change the word pick to squash (or just s) for all but the first commit. This tells Git to merge the changes from these commits into the first commit. Your list will look like this:

!!! Terminal 
     pick ab12c34 Commit message 1

     squash de56f78 Commit message 2
      
     squash gh90i12 Commit message 3

8.Save and close the editor.

9.Git will prompt you to modify the commit message for the new combined commit. You can choose to keep one of the existing commit messages or edit it to create a new one.

10.Save and close the editor again.

11.Git will perform the rebase, combining the selected commits into a single commit. If there are any conflicts during the rebase, you'll need to resolve them as instructed by Git.

12.Once the rebase is complete, you will have one consolidated commit with the changes from the previous commits.

13.If you had already pushed the old commits to a remote repository, you may need to force push the updated branch.


- Link to Refer [Document](https://prasad-k-pawar.medium.com/how-to-combine-multiple-git-commits-into-one-c04c67367a36)


