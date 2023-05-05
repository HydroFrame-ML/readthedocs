
make html
make -C clean
make -C html
rsync -av html/ docs
rm -rf html
