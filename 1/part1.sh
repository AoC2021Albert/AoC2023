(echo -ne "expr " ; paste <(sed 's/^[^0-9]*\([0-9]\).*$/\1/' in.raw) <(sed 's/^.*\([0-9]\)[^0-9]*$/\1/' in.raw)| sed 's/\t//' | sed 's#$# + \\#' ; echo 0) | bash
