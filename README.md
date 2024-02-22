# CourseReviewETH

If you wanna see the forum in action: https://n.ethz.ch/~lteufelbe/coursereview/

Code for forum to rate and review all courses in ETHZ. Works with SwitchAAI of nethz website to verify users.  
Reviews will need to be approved before being released and the UniqueId (different per university, for ETH: "string-of-numbers@ethz.ch") will be saved with review for users to be able edit them later on.  
Nothing else is saved to still somewhat have anonymity as you cannot (easily) find the UniqueId of a Student.


## Run Flask app

1. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Run Flask app
```bash
flask run
```