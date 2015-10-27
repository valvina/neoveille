# neoveille
a bunch of files to analyze rss feeds : 
- merge files by year-month
- tokenize them into sentences and words
- pos-tag the files
- identify formal neologisms

File to be considered (26/10/2015)
- file_find_neologisms.py : see description
- create_merge_files.py : create files by year-month from individuals files into subdirectory by language (to be tested on tar files from neoveille tal server)
- documentclass.py : base class for document object (work in progress)


test_data contient des fichiers test pour les différents traitements : segmentation, repérage néologismes. il faut mettre dedans des cas reguliers et des cas tordus
corpus contient des extraits de corpus pour faire les tests également.
