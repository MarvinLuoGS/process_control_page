# Snippets for process_control_page

A page controling process in experiments conducted using otree. Experimenter input 'password' to allow participants move on to next page.

## Usage

This page can be used in experiment containing different tasks. Before each task, all the participants can't procedd, and the experiment can give instructions about the following task. After introducing the task, experimenter can input the password and tell participants click on the button to proceed.

If there are N participants, the number of participants' link should be N+1, including a link for experimenter.
It acts as if the experimenter 'participate' in the experiment. All the experiment need to do is input the password and allow other participants to proceed.

The 'psswd' works kind of like a one-time password. After the participants move on to next page, the 'psswd' field will be set to initial value. So the same password can be used again. In other words, the ControlPage can be used multiple times.
