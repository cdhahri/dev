$script = <<SCRIPT
sudo apt-get update

sudo apt-get -y install build-essential \
                        python3 \
                        python3-dev \
                        python3-pip

sudo pip3 install --upgrade pip

sudo pip3 install nose \
                  numpy \
                  scipy \
                  scikit-learn \
                  Theano \
                  tensorflow
SCRIPT

Vagrant.configure("2") do |cluster|

    cluster.vm.define "ml" do |machine|
        machine.vm.box = "ubuntu/trusty64"
        machine.vm.hostname = "ml"

        machine.vm.provision "shell", inline: $script

        machine.vm.provider "virtualbox" do |vbox|
            vbox.name = "ml"
            vbox.memory = 1024
        end
    end

end
