
#!/bin/bash
#
# organizer.sh
# Archives the current grades.csv into archive/ with a timestamped name,
# resets grades.csv to a fresh empty file, and logs the operation.
#
# Usage: ./organizer.sh

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created archive directory: $ARCHIVE_DIR"
fi

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found. Nothing to archive."
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"

mv "$SOURCE_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"

# Workspace reset: fresh empty grades.csv for the next batch of grades
: > "$SOURCE_FILE"

echo "$TIMESTAMP | original: $SOURCE_FILE | archived as: $ARCHIVE_DIR/$ARCHIVED_NAME" >> "$LOG_FILE"

echo "Archived '$SOURCE_FILE' to '$ARCHIVE_DIR/$ARCHIVED_NAME'."
echo "A fresh, empty '$SOURCE_FILE' has been created."
echo "Logged operation to '$LOG_FILE'."
