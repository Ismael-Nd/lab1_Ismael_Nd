### 1. Python application

Run the script and enter the CSV filename when prompted:

```bash
python grade-evaluator.py
```

```
Enter the name of the CSV file to process like grades.csv
```

The script will:

1. **Grade Validation** : check every assignment's score is between 0 and 100.
2. **Weight Validation** : confirm all weights sum to exactly 100, with
  Summative assignments totaling 40 and Formative assignments totaling 60.
3. **GPA Calculation** : compute the weighted Total Grade and
  `GPA = (Total Grade / 100) * 5.0`.
4. **Final Decision** : printing passed or failed. A student passes only if
  their weighted average is at or above 50% in **both** the summartive and  formative categories.
5. **Resubmission Logic** : identify any formtive assignment scoring below
  50%, and list the ones with the highest weight as eligible for  
   resubmission.

### 2. Bash script

```bash
chmod +x organizer.sh
./organizer.sh
```

