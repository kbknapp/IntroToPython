# Useful Commands for Linux

## find and delete duplicate files
```bash
find -not -empty -type f -printf "%s\n" | sort -rn | uniq -d | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate | cut -f3-100 -d '' | tr '\n.' '\t.' | sed 's/\t\t/\n/g' | cut -f2-100 | tr '\t' '\n' | perl -i -pe 's/([ (){}-])/\\$1/g' | perl -i -pe 's/\"/\\'\"/g' | xargs -pr rm -v
```

## copy files
```bash
cp <from> <to>
```

## copy whole directories
```bash
cp -R <from> <to>
```

## rename files and directories 
```bash
mv <old name> <new name>
```

## move files and directories 
```bash
mv <from> <to>
```

## delete files
```bash
rm <files>
```

## delete directoires
```bash
rm -r <dir>
```

## link files link directories symlinks
```bash
ln -s <object> <new link>
```

## show hidden files
```bash
ls -a
```

## show current directory
```bash
pwd
```

## update arch linux
```bash
sudo pacman -Syu
```

## install
```bash
yaourt -S <app>
```

## search for app software
```bash
yaourt -Ss <app name>
```

## list installed software
```bash
sudo pacman -Qs
```

## count lines of file
```bash
wc -l <file>
```

## search contents of file for word
```bash
cat <file> | grep 'word'
```

## search for file
```bash
find <start dir> -name 'name' -type f
```

## show environemnt variables
```bash
env
```

## set environment variable
```bash
export VAR_NAME=value
```

## make file executable
```bash
chmod +x <file>
```