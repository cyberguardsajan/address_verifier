# Regex Patterns for Python

A table of common regex patterns used in Python:

**Pattern**            | **Description**                                               | **Example**                           | **Matches**                                 
------------------------|---------------------------------------------------------------|---------------------------------------|--------------------------------------------- 
`.`                    | Any character except a newline                                | `a.c`                                 | `abc`, `a-c`                              
`^`                    | Matches the start of a string                                 | `^Hello`                              | `Hello world` (if the string starts with `Hello`) 
`$`                    | Matches the end of a string                                   | `world$`                              | `Hello world` (if the string ends with `world`) 
`*`                    | Matches 0 or more occurrences of the preceding element        | `a*`                                  | `a`, `aa`, `aaa`, `b`                      
`+`                    | Matches 1 or more occurrences of the preceding element        | `a+`                                  | `a`, `aa`, `aaa`                           
`?`                    | Matches 0 or 1 occurrence of the preceding element            | `a?`                                  | ``, `a`                                    
`{n}`                  | Matches exactly `n` occurrences of the preceding element      | `a{3}`                                | `aaa`                                      
`{n,}`                 | Matches `n` or more occurrences of the preceding element       | `a{2,}`                               | `aa`, `aaa`, `aaaa`                        
`{n,m}`                | Matches between `n` and `m` occurrences of the preceding element | `a{2,4}`                             | `aa`, `aaa`, `aaaa`                        
`[...]`                 | Matches any one of the enclosed characters                     | `[abc]`                               | `a`, `b`, `c`                              
`[^...]`                | Matches any character not enclosed                             | `[^0-9]`                              | `a`, `@`                                   
`()`                   | Groups patterns together                                     | `(abc)+`                              | `abc`, `abcabc`                            
`\d`                   | Matches any digit (equivalent to `[0-9]`)                      | `\d{2}`                               | `12`, `34`                                 
`\D`                   | Matches any non-digit character                                | `\D`                                  | `a`, `!`                                   
`\w`                   | Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`) | `\w+`                                | `abc123`, `a_b`                            
`\W`                   | Matches any non-alphanumeric character                        | `\W`                                  | `!`, `@`                                   
`\s`                   | Matches any whitespace character                               | `\s`                                  | ` ` (space), `\t` (tab)                    
`\S`                   | Matches any non-whitespace character                          | `\S`                                  | `a`, `1`, `!`                              
`\b`                   | Matches a word boundary                                      | `\bword\b`                             | `word`, `wording` (matches whole word `word`) 
`\B`                   | Matches a non-word boundary                                  | `\Bend`                                | `ending`, `bend` (matches `end` within `ending`) 



# Regex Pattern Explanation

## Regex Pattern
`r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`

## Explanation

- `^[a-zA-Z0-9_.+-]+`: Matches the local part of the email (before the @ symbol). It can include letters, digits, underscores, periods, pluses, and hyphens.
- `@[a-zA-Z0-9-]+`: Matches the domain name (after the @ symbol). It can include letters, digits, and hyphens.
- `\.[a-zA-Z0-9-.]+$`: Matches the top-level domain (e.g., .com). It can include periods, letters, and digits.

## `re.match`

Checks if the entire string matches the regex pattern from the beginning. Returns a match object if the pattern matches, otherwise None.

