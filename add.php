<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; object-src 'none'">
    <title>Review</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link href="../default.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <div id="header">
        <h1>CourseReview</h1>
        <h2>&nbsp;</h2>
    </div>
    <?php include 'includes/menu.php' ?>
    <?php
    $surname = $_SERVER["surname"];
    $name = $_SERVER["givenName"];
    $val = $_SERVER["uniqueID"];
    ?>
    <div id="content">
        <div id="columnA">
            <p><b>Add a CourseReview here.</b><br>

            <form method="post" action="submit.php">
                <fieldset>
                    <legend>Review</legend>
                    <p>
                        <label for="course">Course number:</label><br>
                        <input list="courses" id="course" name="course" placeholder="252-0027-00L" pattern="[A-Z0-9]{3}-[A-Z0-9]{4}-[A-Z0-9]{3}( .*)?" size="80" required>
                        <datalist id="courses">
                            <?php
                            $db = new SQLite3('CourseReviews.db');
                            $stmt = $db->prepare("SELECT * FROM COURSES");
                            $result = $stmt->execute();

                            while ($row = $result->fetchArray()) {
                            ?>
                                <option value="<?php echo "$row[0] $row[1]"; ?>">
                                <?php
                            }
                            $db->close();
                                ?>
                        </datalist>
                    </p>
                    <p>
                        <label>
                            Review:
                            <br>
                            <textarea name="review" cols="50" rows="3" placeholder="For some very hard, while others who already have knowledege about the content it is very easy." required></textarea>
                        </label>
                    </p>
                    <p>
                        <button type="submit">Submit</button>
                    </p>
                </fieldset>
            </form>

        </div>
    </div>
    
    <?php include 'includes/footer.php'; ?>
</body>
</html>