;;;; kram.asd

(asdf:defsystem #:kram
  :description "Hyper parameter oracle"
  :author "Abhinav Tushar <lepisma@fastmail.com>"
  :license  "GPLv3"
  :version "0.0.1"
  :serial t
  :components ((:file "package")
               (:file "kram")))
